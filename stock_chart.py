import matplotlib.pyplot as plt

def load_data(filename):
    x_data = []
    y_data = []
    # load file
    with open(filename, "r") as in_file:
        in_file.readline()     # read and throw away the first line
        lines = in_file.readlines()   # read all lines in the file
        for line in lines:
            temp_data = line.split(",")   # string becomes a list
            stock_date = temp_data[0]     # 1st column - date
            stock_price = float(temp_data[5])    # 6th column - adj close
            x_data.append(stock_date)
            y_data.append(stock_price)

    return x_data, y_data

def plot_chart(x_data, y_data):
    plt.plot(x_data, y_data)
    plt.title("Stock Chart")
    plt.xlabel("Dates")
    plt.ylabel("Prices (USD")
    plt.show()


def main():

    # 1. extract data from the file into 2 lists (x_data, y_data)
    x_data, y_data = load_data("XOM.csv")

    # 2. plot the chart using dates, prices
    plot_chart(x_data, y_data)


main()   # call the main method