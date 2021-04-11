from flask import Flask, request, jsonify
from text_similarity import TextSimilarity

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': "welcome to Text Similarity Application"})


@app.route('/score', methods=['POST'])
def get_similarity_score():
    try:
        content = request.get_json()
        Text_1 = content['Text_1']
        Text_2 = content['Text_2']

        text_sim = TextSimilarity(Text_1, Text_2)
        similarity_score = []

        for ngram_len in range(2, 5):
            score = text_sim.calculate_score(ngram_len)
            similarity_score.append(score)

        max_score = -1
        ngram = 0
        for i in range(0, len(similarity_score)):
            if similarity_score[i] > max_score:
                max_score = similarity_score[i]
                ngram = i + 2

        output = {'Similarity Score': max_score, 'Ngram': ngram}
        return output
    except:
        return 'Input should be in {"Text_1": "<text>", "Text_2": "<text>"}', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
