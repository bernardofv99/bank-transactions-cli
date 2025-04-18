from collections import defaultdict

import pandas as pd

from app.utils import format_money


class TransactionProcessor:
    """
    Clase encargada de procesar transacciones bancarias desde un archivo CSV
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []

    def load(self):
        """
        Carga las transacciones desde el archivo CSV usando pandas
        """
        df = pd.read_csv(self.file_path)
        for _, row in df.iterrows():
            self.transactions.append({
                'id': int(row['id']),
                'type': str(row['tipo']),
                'amount': format_money(row['monto'])
            })

    def get_balance(self):
        """
        Calcula el balance total: Créditos - Débitos
        """
        total_credit = sum(t['amount'] for t in self.transactions if t['type'] == 'Crédito')
        total_debit = sum(t['amount'] for t in self.transactions if t['type'] == 'Débito')
        return total_credit - total_debit

    def get_max_transaction(self):
        """
        Devuelve la transacción con mayor monto
        """
        return max(self.transactions, key=lambda t: t['amount'])

    def get_transaction_counts(self):
        """
        Retorna el conteo de transacciones por tipo
        """
        counts = defaultdict(int)
        for t in self.transactions:
            counts[t['type']] += 1
        return counts

    def generate_report(self):
        """
        Construye el reporte final en la terminal
        """
        balance = self.get_balance()
        max_tx = self.get_max_transaction()
        counts = self.get_transaction_counts()
        return (
            "Reporte de Transacciones\n"
            "---------------------------------------------\n"
            f"Balance Final: {balance:.2f}\n"
            f"Transacción de Mayor Monto: ID {max_tx['id']} - {max_tx['amount']:.2f}\n"
            f"Conteo de Transacciones: Crédito: {counts['Crédito']} Débito: {counts['Débito']}\n"
        )
