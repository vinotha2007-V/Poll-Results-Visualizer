from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import poll_counts
from src.visualization import plot_poll_results

df = load_data("data/raw/poll_data.csv")
df = preprocess(df)

counts = poll_counts(df)
plot_poll_results(counts)
