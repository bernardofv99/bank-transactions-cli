import pytest
from app.processor import TransactionProcessor

@pytest.fixture
def sample_data(tmp_path):
    csv_content = "id,tipo,monto\n1,Crédito,100\n2,Débito,50\n3,Crédito,200"
    file_path = tmp_path / "test_data.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    return file_path

def test_balance(sample_data):
    processor = TransactionProcessor(sample_data)
    processor.load()
    assert processor.get_balance() == 250

def test_max_transaction(sample_data):
    processor = TransactionProcessor(sample_data)
    processor.load()
    max_tx = processor.get_max_transaction()
    assert max_tx['id'] == 3
    assert max_tx['amount'] == 200

def test_transaction_counts(sample_data):
    processor = TransactionProcessor(sample_data)
    processor.load()
    counts = processor.get_transaction_counts()
    assert counts['Crédito'] == 2
    assert counts['Débito'] == 1
