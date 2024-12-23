def read_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def plot_graph(data):
    import matplotlib.pyplot as plt
    plt.plot(data['x'], data['y'])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Graph')
    plt.show()

def main():
    data = read_data('data.csv')  # Replace with your data file path
    plot_graph(data)

if __name__ == "__main__":
    main()