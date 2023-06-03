from mongoengine import Document, StringField, DynamicField, EmbeddedDocumentListField, EmbeddedDocumentField, EmbeddedDocument, IntField


class Request (EmbeddedDocument):
    headers = DynamicField()
    device_id = StringField()


class Data (EmbeddedDocument):
    name = StringField()
    request = EmbeddedDocumentField(Request)
    expected = DynamicField()
    expectedStatusCode = IntField()


class Deletes(Document):
    _id = StringField()
    name = StringField()
    endpoint = StringField()
    data = EmbeddedDocumentListField(Data)
