# ⚽ Football Player Scouting AI

## 🚀 **Overview**
Football Player Scouting AI is a **Streamlit-based web application** that helps scouts, coaches, and analysts find **top-performing football players** based on various criteria. By selecting an **age range, league, and player position**, users can retrieve a list of **top-ranked players** along with **radar charts** visualizing their key performance metrics.

## 🎯 **Features**
✅ Load and analyze player performance data from `updated_football_player_stats.csv`.
✅ Use trained **machine learning models** to rank players based on performance.
✅ Select players based on position: **Forward, Midfielder, Defender, or Goalkeeper**.
✅ Filter by **age range and league**.
✅ Display **top 5 players** based on AI prediction.
✅ Generate **radar charts** for selected players.
✅ Interactive **UI built with Streamlit** for a seamless user experience.

## 🛠 **Tech Stack**
- 🐍 **Python**: Core programming language
- 🖥️ **Streamlit**: UI framework
- 📊 **Pandas**: Data manipulation
- 🔢 **NumPy**: Numerical computations
- 📈 **Matplotlib**: Radar chart visualizations
- 📦 **Pickle**: Model loading
- 🖼️ **PIL**: Image handling

## ⚙️ **Installation**
### 🔗 **Prerequisites**
Ensure you have **Python 3.x** installed. Install the required dependencies using:
```sh
pip install streamlit pandas numpy matplotlib pillow
```

### 📂 **Clone the Repository**
```sh
git clone https://github.com/your-repo/football-scouting-ai.git
cd football-scouting-ai
```

### ▶️ **Running the Application**
```sh
streamlit run app.py
```

## 📁 **File Structure**
```
├── 📌 best_fw_model.pkl      # Trained Forward model
├── 📌 mf_model.pkl           # Trained Midfielder model
├── 📌 df_model.pkl           # Trained Defender model
├── 📌 gk_model.pkl           # Trained Goalkeeper model
├── 📊 updated_football_player_stats.csv  # Player dataset
├── 🖼️ Scout.jpg              # Header image for UI
├── 📝 app.py                 # Main application script
└── 📖 README.md              # Project documentation
```

## 🏆 **How to Use**
1. **Launch the app** using `streamlit run app.py`.
2. Use the **sidebar** to set scouting criteria:
   - 🎯 **Select age range**
   - 🌍 **Choose a league**
   - ⚽ **Pick a player position**
3. Click **"Scout Players"** to get **AI-ranked players**.
4. View the **top 5 players** and their **radar charts**.

## 📊 **Example Output**
- **Player Table**: Displays **name, age, league, and key stats**.
- **Radar Chart**: Visualizes a player's strengths across **multiple performance metrics**.

## 🤝 **Contributing**
🚀 Contributions are welcome! Feel free to submit **issues and pull requests**.

---
### 👤 **Author**
Developed by **Tosho (AI Scouting Application)**
