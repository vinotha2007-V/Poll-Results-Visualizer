import matplotlib.pyplot as plt

def plot_poll_results(counts):
    counts.plot(kind='bar')
    plt.title("Poll Results")
    plt.xlabel("Options")
    plt.ylabel("Votes")
    plt.show()
