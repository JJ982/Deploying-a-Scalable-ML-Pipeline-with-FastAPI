import pytest
from sklearn.datasets import make_classification
from ml.model import train_model
from ml.data import apply_label

def test_train_model():
    """
    This test checks that the function creates a model.
    """
    X_train, y_train = make_classification(
        n_samples=80, 
        random_state=42
    )
    model = train_model(X_train, y_train)
    assert model is not None

def test_apply_label_returns_expected_values_with_valid_inputs():
    """
    This test checks that when the binary label passed is 0, <=50K is returned and when the binary label is 1, >50K is returned.
    """
    assert apply_label([0]) == "<=50K"
    assert apply_label([1]) == ">50K"

def test_apply_label_raises_error_on_invalid_input():
    """
    This test checks that when the binary label passed is neither 0 nor 1, "Invalid input" is returned.
    """
    assert apply_label([2]) == "Invalid input"
