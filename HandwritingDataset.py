"""Handwritten digit classification using scikit-learn's digits dataset."""

from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main() -> None:
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42, stratify=digits.target
    )
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    print("Handwriting Dataset (Digits) classifier")
    print(f"Training samples: {len(x_train)} | Test samples: {len(x_test)}")
    print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")
    print("\nClassification report:\n", classification_report(y_test, predictions))


if __name__ == "__main__":
    main()
