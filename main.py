import argparse
from model.cnn_model import ImageClassifier
from utils.data_preprocessing import DataLoader
from utils.train_utils import train_model, evaluate_model

def main():
    parser = argparse.ArgumentParser(description='Image Classification Training')
    parser.add_argument('--data_dir', type=str, required=True, help='Path to dataset directory')
    parser.add_argument('--epochs', type=int, default=10, help='Number of training epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    args = parser.parse_args()

    # Initialize data loader
    data_loader = DataLoader(args.data_dir, batch_size=args.batch_size)
    train_data, val_data = data_loader.load_data()

    # Initialize model
    model = ImageClassifier(num_classes=data_loader.num_classes)

    # Train the model
    trained_model = train_model(model, train_data, val_data, epochs=args.epochs)

    # Evaluate the model
    evaluate_model(trained_model, val_data)

if __name__ == '__main__':
    main()