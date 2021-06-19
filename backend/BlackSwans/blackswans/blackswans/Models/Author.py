from neo4j import GraphDatabase


class Author:

    def __init__(self, uri, _user, _password):
        self.driver = GraphDatabase.driver(uri, auth=(_user, _password))

    def close(self):
        self.driver.close()

    def get_authors(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_some_authors)
            authors = []
            for record in result:
                authors.append(record)
            return authors

    @staticmethod
    def _get_some_authors(tx):
        query = (
            "MATCH (a:Author) "
            "RETURN a.author_name AS name"
        )
        result = tx.run(query)
        return [record["name"] for record in result]


