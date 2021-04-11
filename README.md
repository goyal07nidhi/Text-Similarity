# Text Similarity Score
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

---
## Getting Started
The Goal of this challenge is to build an application to find the similarity score between two texts.

Using flask app to demonstrate this service. Application takes as inputs two texts and uses a metric to determine how similar they are. 
Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.


## Tasks performed

- Task 1: Read input text in json format
- Task 2: Preprocess the input texts (remove stopwords and punctuation)
- Task 3: Generate N-grams for both texts
- Task 4: Calculate similarity score
- Task 5: Create Flask app
- Task 6: Dockerize the end point

>NOTE: Made number of decisions as I developed this solution:

1. I removed all the punctuations at the time of preprocessing.
   
2. In the similarity comparison, all english words matter except stop words. I removed stop words in the preprocessing step.

3. The ordering of words does matter. Instead of doing a word for word comparison, I tried in context of the semantics similarity by considering phrase(s).

4. I used the formula Intersection(A, B) / Union(A, B) to calculate similarity score for two texts A and B.
   Intersection(A, B) calculates the common n-grams whereas Union(A, B) calculates the unique n-grams across both texts.

5. I leveraged 'list' and 'set' data structures to calculate the similarity of the two texts.

## Flow chart
<img width="618" alt="Screen Shot 2021-04-11 at 3 30 17 AM" src="https://user-images.githubusercontent.com/56357740/114295903-46d33f80-9a76-11eb-8f3b-c644cec64256.png">

## Project Structure
```
Text-Similarity/
├── app/
│   ├── app.py
│   ├── stopwords.txt
│   └── text_similarity.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## Build
To build the application, run the following commands:
### Local:
1. ` git clone https://github.com/goyal07nidhi/Text-Similarity.git`
2. `cd Text-Similarity/`
3. `docker build -t nidhi2019/text-similarity:latest .` 

### From Dockerhub:
1. `docker pull nidhi2019/text-similarity`


## Run
1.`docker run -it --rm -p 5000:5000 nidhi2019/text-similarity'`

## Test
### Postman:
1. Send a POST request to `http://0.0.0.0:5000/score'` with the JSON input in the body

### Curl:
1. `curl localhost:5000/score -d '{"Text_1": "<text>", "Text_2": "<text>"}' -H 'Content-Type: application/json'`
2. e.g. `curl localhost:5000/score -d '{"Text_1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you.", "Text_2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}' -H 'Content-Type: application/json'`