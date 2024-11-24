# Fake Job Detection Using Shallow and Deep Learning  

## Overview  
Fake job postings are a growing concern in the employment sector, leading to financial and emotional losses for job-seekers. This project uses a combination of machine learning (ML) and natural language processing (NLP) techniques to build a robust system that detects fraudulent job postings with high accuracy.  

## Features  
- **Integration of Shallow and Deep Learning**: Combines TF-IDF vectorization with BERT embeddings for enhanced textual analysis.  
- **Balanced Dataset Resampling**: Addresses class imbalance by resampling to ensure equal representation of fraudulent and non-fraudulent job postings.  
- **Contextual Clustering and Topic Modeling**: Groups job postings to provide insights and help identify patterns of fraudulent jobs.  
- **Random Forest Interpretability**: Leverages Random Forest for feature importance to improve detection and provide insights into fraudulent activities.  
- **Real-Time Detection**: Provides immediate feedback to users, alerting them to potentially fraudulent job postings.  

## System Architecture  
The system is composed of the following components:  
1. **Data Ingestion Module**: Collects job posting data from various sources.  
2. **Feature Extraction Module**: Extracts numerical and semantic features using TF-IDF and BERT embeddings.  
3. **Model Training Module**: Trains machine learning models using a balanced dataset.  
4. **Inference Engine**: Classifies new job postings as legitimate or fraudulent.  
5. **User Interface**: Displays results and provides fraud detection guidance.  

## Methodology  
1. **Data Preprocessing**:  
   - Cleans and preprocesses the data to handle missing values and normalize text.  
   - Balances the dataset with resampling techniques.  

2. **Feature Extraction**:  
   - Converts text data into numerical features using TF-IDF.  
   - Uses BERT embeddings for a deeper semantic understanding.  

3. **Model Training**:  
   - Employs Random Forest for interpretability.  
   - Integrates deep learning models for more complex pattern detection.  

4. **Clustering and Topic Modeling**:  
   - Groups job postings based on textual similarities to enhance contextual understanding.  

5. **Evaluation Metrics**:  
   - Uses accuracy, precision, recall, and F1-score to evaluate performance.  

## Benefits  
- **Job Seeker Protection**: Identifies fraudulent job postings, safeguarding job-seekers from scams.  
- **Enhanced Accuracy**: Reduces false positives and improves fraud detection through advanced ML techniques.  
- **Scalability**: Capable of handling large datasets and continuously learning from new data.  
- **Fraud Analysis**: Provides insights into locations and patterns associated with fraudulent jobs.  

## Novel Features  
1. **Integration of TF-IDF with BERT**: Combines traditional and modern NLP techniques for superior analysis.  
2. **Balanced Dataset**: Resampling ensures improved performance by addressing class imbalance.  
3. **Contextual Clustering**: Groups similar postings for better insights into fraudulent patterns.  
4. **Random Forest for Interpretability**: Balances performance and feature importance analysis.  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/fake-job-detection.git  
   cd fake-job-detection  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the application:  
   ```bash  
   python app.py  
   ```  

![img](https://github.com/user-attachments/assets/5e5013f7-aa61-4387-b678-11e6f862c66c)

## Usage  
- Upload a dataset of job postings in CSV format.  
- The system will preprocess and classify postings as legitimate or fraudulent.  
- Visualizations and metrics will help analyze results.  

## Dataset  
- The project requires a dataset containing job posting information (e.g., title, description, location).  

## Contributing  
Contributions are welcome! Please fork the repository and submit a pull request with your changes.  

## License  
This project is licensed under the [MIT License](LICENSE).  

## Keywords  
Employment Scam Detection, Machine Learning, Natural Language Processing, Job Fraud, Deep Learning, Random Forest, BERT Embeddings, TF-IDF Vectorization, Clustering, Topic Modeling  


