import pytest
from sec_class import Secretary
from sec_data import documents, directories, command_help


@pytest.fixture()
def app():
    app = Secretary(documents, directories, command_help)
    return app


@pytest.fixture()
def doc():
    test_data = {
        'doc': {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        'doc_shelf': '1',
        'new_doc': {'type': 'passport', 'number': '456781', 'name': 'Alex'},
        'new_doc_shelf': '3',
        'new_shelf': '4'
    }
    return test_data


class Test:

    def test_get_people(self, app, doc):
        assert app.get_people(doc['doc']['number']) == doc['doc']['name']

    def test_get_shelf(self, app, doc):
        assert app.get_shelf(doc['doc']['number']) == doc['doc_shelf']

    def test_add(self, app, doc):
        app.add(
            doc['new_doc']['type'],
            doc['new_doc']['number'],
            doc['new_doc']['name'],
            doc['new_doc_shelf']
        )
        assert doc['new_doc'] in app._docs
        assert doc['new_doc']['number'] in app._dirs[doc['new_doc_shelf']]

    def test_delete(self, app, doc):
        app.delete(doc['doc']['number'])
        assert doc not in app._docs
        assert doc['doc']['number'] not in doc['doc_shelf']

    def test_move(self, app, doc):
        app.move(doc['doc']['number'], doc['new_doc_shelf'])
        assert doc['doc']['number'] in app._dirs[doc['new_doc_shelf']]

    def test_add_shelf(self, app, doc):
        app.add_shelf(doc['new_shelf'])
        assert doc['new_shelf'] in app._dirs.keys()
