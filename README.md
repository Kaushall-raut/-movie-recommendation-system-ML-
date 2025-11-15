# Movie Recommender System

A movie recommendation system built using Python and Streamlit.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/movie-recommender.git
```
2. Navigate to the project directory:
```
cd movie-recommender
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```
streamlit run app.py
```
2. The app will open in your default web browser.
3. Select a movie from the dropdown menu and click the "Recommend" button to see the top 5 recommended movies.

## API

The app uses the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to fetch movie poster images. You'll need to obtain an API key and replace `'78a0995fd10ee83ab18023f06a9bc32b'` in the `fetch_image()` function in `app.py`.

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

No automated tests have been provided for this project. You can manually test the app by running it and interacting with the user interface.
