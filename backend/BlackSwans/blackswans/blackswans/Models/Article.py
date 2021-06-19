from neo4j import GraphDatabase


class Article:

    def __init__(self, uri, _user, _password):
        self.driver = GraphDatabase.driver(uri, auth=(_user, _password))

    def close(self):
        self.driver.close()

    def get_top10_papers_by_pagerank_by_cites(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_top10_papers_by_pagerank_by_cites)
            top10 = []
            for record in result:
                top10.append(record)
            return top10

    @staticmethod
    def _get_top10_papers_by_pagerank_by_cites(tx):
        query = (
            "MATCH (p:Paper)<-[r:HAS_PUBLISHED]-(a:Author) "
            "RETURN p.title as title, p.pagerankByCites as rank, a.author_name as author, r "
            "ORDER BY rank DESC "
            "LIMIT 10"
        )
        result = tx.run(query)
        return [{"paper": {"title": row["title"], "pagerank": row["rank"]}, "author": row["author"]} for row in result]

    def get_top10_papers_by_pagerank_by_journal(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_top10_papers_by_pagerank_by_journal)
            top10 = []
            for record in result:
                top10.append(record)
            return top10

    @staticmethod
    def _get_top10_papers_by_pagerank_by_journal(tx):
        query = (
            "MATCH (j:Journal)<-[:PUBLISHED_AT]-(p:Paper) "
            "RETURN p.title as title, p.pagerankByJournal as pagerank, j.venue as journal "
            "ORDER BY pagerank DESC "
            "LIMIT 10"
        )
        result = tx.run(query)
        return [{"paper": {"title": row["title"], "pagerank": row["pagerank"]}, "journal": row["journal"]}
                for row in result]



