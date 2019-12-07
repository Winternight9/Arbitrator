function setupView() {
  results.data.forEach(question => {
    addQuestionLabel(question.label);

    switch (question.type) {
      case "text":
        addTextQuestionResult(question.answers);

        break;
      case "choice":
        addChoiceQuestionResult(question.answers);

        break;
      default:
        alert("Error");
    }
  });
}

function addQuestionLabel(label) {
  const questionContainer = getQuestionContainer();

  questionContainer.append(createLabel(label));
}

function addTextQuestionResult(results) {
  const questionContainer = getQuestionContainer();

  const answerContainer = document.createElement("div");
  answerContainer.className = "text-result-container";

  results.forEach(answer => {
    const p = document.createElement("p");
    p.className = 'result'

    p.textContent = answer;

    answerContainer.append(p);
  });

  questionContainer.append(answerContainer);
}

function addChoiceQuestionResult(results) {
  const questionContainer = getQuestionContainer();

  const answerContainer = document.createElement("div");
  answerContainer.className = "choice-result-container";

  results.forEach(answer => {
    const p = document.createElement("p");
    p.className = 'result'

    p.textContent = `${answer.label} — vote: ${answer.voteCount}`;

    answerContainer.append(p);
  });

  questionContainer.append(answerContainer);
}

function getQuestionContainer() {
  return document.getElementById("question-container");
}

function createLabel(value) {
  const label = document.createElement("label");

  label.textContent = value;

  return label;
}

setupView();
