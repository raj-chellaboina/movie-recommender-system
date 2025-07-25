# Movie Recommender System

A simple content-based movie recommender web application built with Python and Streamlit. This app suggests five movies similar to a selected movie and displays their poster images.

---

## Features

- **Movie Recommendation:** Get five similar movies based on your selection.
- **Poster Display:** View movie posters alongside recommendations.
- **Interactive UI:** Easy-to-use interface powered by Streamlit.

---

## Project Structure

```
movie-recommender-system/
│
├── app.py                # Main Streamlit application
├── movies_dict.pkl       # Pickled dictionary containing movie data
├── similarity.pkl        # Pickled similarity matrix for recommendations
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## How It Works

1. **Data Loading:**  
   Loads movie data and a similarity matrix from pickle files.

2. **Recommendation Logic:**  
   When a user selects a movie, the app finds the most similar movies using the similarity matrix.

3. **Poster Fetching:**  
   For each recommended movie, a poster image is displayed (currently uses a placeholder image).

4. **User Interface:**  
   The app provides a dropdown to select a movie and displays recommendations in a visually appealing layout.

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raj-chellaboina/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## Deployment

You can deploy this app for free using [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code and data files to GitHub.
2. Sign in to Streamlit Cloud and create a new app from your repository.

---

## Notes

- The poster fetching function currently returns a placeholder image. You can enhance it by integrating with the [TMDB API](https://www.themoviedb.org/documentation/api).
- Ensure `movies_dict.pkl` and `similarity.pkl` are present in the project directory.

---

## License

This project is licensed under the MIT License.

---

## Download Required Data Files

This project requires two data files that are too large for GitHub.  
Please download them from the links below and place them in your project folder (where `app.py` is located):

- [movies_dict.pkl](https://drive.google.com/file/d/1D0U9vuPSUGIhxYfkhySu7x07cv4juyPr/view?usp=drive_link)
- [similarity.pkl](https://drive.google.com/file/d/1L8JLn7DW4oVenheA5Kp_5mRwfjjnMkfv/view?usp=drive_link)

**After downloading, place both files in the root directory of your project.**

## Author

[raj-chellaboina](https://github.com/raj-chellaboina)# movie-recommender-system
# movie-recommender-system
