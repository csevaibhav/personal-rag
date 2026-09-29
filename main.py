"""CLI entrypoint for querying the personal RAG chatbot locally."""
import sys

from src.pipeline import answer_query


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python main.py "your question here"')
        sys.exit(1)
    query = " ".join(sys.argv[1:])
    print(answer_query(query))


if __name__ == "__main__":
    main()
