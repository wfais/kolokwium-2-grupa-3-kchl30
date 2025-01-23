def transform_texts(texts):
    """
    Napisz funkcję, która przyjmuje listę napisów i zwraca listę przekształconych tekstów:
      1) bez pustych
      2) zamienione na wielkie litery,
      3) odwrócone (w sensie kolejności znaków).
    """

    filtered_texts = [t for t in texts if t.strip()]

    transformed = map(lambda t: t.strip().upper()[::-1], filtered_texts)

    return list(transformed)

if __name__ == '__main__':
    sample_data = ["hello", "  ", "world", "", "python"]
    result = transform_texts(sample_data)  # ['OLLEH', 'DLROW', 'NOHTYP']
    print("Dla danych:", sample_data)
    print("Wynik   :", result)
