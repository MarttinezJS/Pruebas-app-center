from mongoengine import Document, StringField, DynamicField, EmbeddedDocumentListField, EmbeddedDocumentField, EmbeddedDocument, IntField


class Param (EmbeddedDocument):
    key = StringField()
    value = StringField()


class Request (EmbeddedDocument):
    headers = DynamicField()
    params = EmbeddedDocumentListField(Param)


class Data (EmbeddedDocument):
    name = StringField()
    request = EmbeddedDocumentField(Request)
    expected = DynamicField()
    expectedStatusCode = IntField()


class Gets(Document):
    _id = StringField()
    name = StringField()
    endpoint = StringField()
    data = EmbeddedDocumentListField(Data)
