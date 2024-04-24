
from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utility import pinecone_config


def ingest():
    pass

if __name__=="__main__":
    ingest()