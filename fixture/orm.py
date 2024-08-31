from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from model.group import Group
from model.contact import Contact

Base = declarative_base()


class GroupModel(Base):
    __tablename__ = 'group_list'
    group_id = Column(Integer, primary_key=True, autoincrement=True, name='group_id')
    group_name = Column(String, nullable=True, name='group_name')
    group_header = Column(String, nullable=True, name='group_header')
    group_footer = Column(String, nullable=True, name='group_footer')
    deprecated = Column(DateTime, nullable=True, name='deprecated')
    contacts = relationship("ContactModel", secondary="address_in_groups", back_populates="groups")


class ContactModel(Base):
    __tablename__ = 'addressbook'
    id = Column(Integer, primary_key=True, autoincrement=True, name='id')
    firstname = Column(String, nullable=True, name='firstname')
    lastname = Column(String, nullable=True, name='lastname')
    deprecated = Column(DateTime, nullable=True, name='deprecated')
    groups = relationship("GroupModel", secondary="address_in_groups", back_populates="contacts")


class AddressInGroups(Base):
    __tablename__ = 'address_in_groups'
    id = Column(Integer, ForeignKey('addressbook.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('group_list.group_id'), primary_key=True)


class SQLAlchemyFixture:
    def __init__(self, host, name, user, password):
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{name}')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.group_id), group_name=group.group_name,
                         group_header=group.group_header, group_footer=group.group_footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    def get_group_list(self):
        session = self.get_session()
        groups = session.query(GroupModel).filter(GroupModel.deprecated == '0000-00-00 00:00:00').all()
        session.close()
        return self.convert_groups_to_model(groups)

    def get_contact_list(self):
        session = self.get_session()
        contacts = session.query(ContactModel).filter(ContactModel.deprecated.is_(None)).all()
        session.close()
        return self.convert_contacts_to_model(contacts)

    def get_contacts_in_group(self, group):
        session = self.get_session()
        orm_group = session.query(GroupModel).filter(GroupModel.group_id == group.group_id).first()
        if orm_group is None:
            session.close()
            return []
        contacts = orm_group.contacts
        session.close()
        return self.convert_contacts_to_model(contacts)

    def get_contacts_not_in_group(self, group):
        session = self.get_session()
        orm_group = session.query(GroupModel).filter(GroupModel.group_id == group.group_id).first()
        if orm_group is None:
            session.close()
            return []
        contact_ids_in_group = {contact.id for contact in orm_group.contacts}
        contacts_not_in_group = session.query(ContactModel).filter(
            ContactModel.deprecated.is_(None),
            ContactModel.id.notin_(contact_ids_in_group)
        ).all()
        session.close()
        return self.convert_contacts_to_model(contacts_not_in_group)

    def get_contacts_not_in_any_group(self):
        session = self.get_session()
        contacts_with_groups_ids = session.query(ContactModel.id).join(AddressInGroups).distinct().subquery()
        contacts_not_in_any_group = session.query(ContactModel).filter(
            ContactModel.deprecated.is_(None),
            ContactModel.id.notin_(contacts_with_groups_ids)
        ).all()
        session.close()
        return self.convert_contacts_to_model(contacts_not_in_any_group)
