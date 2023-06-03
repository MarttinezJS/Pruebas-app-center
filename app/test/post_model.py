from mongoengine import Document, StringField, DynamicField, EmbeddedDocumentListField, EmbeddedDocumentField, EmbeddedDocument, IntField


class Request (EmbeddedDocument):
    body = DynamicField()
    uid = StringField()


class Data (EmbeddedDocument):
    name = StringField()
    request = EmbeddedDocumentField(Request)
    expected = DynamicField()
    expectedStatusCode = IntField()


class Posts(Document):
    _id = StringField()
    name = StringField()
    endpoint = StringField()
    data = EmbeddedDocumentListField(Data)
