const QuestionType = {
  text: 0,
  choice: 1
};

function addQuestion() {
  const questionContainer = document.getElementById("question-container");
  const questionType =
    QuestionType[document.getElementsByName("new-question-type")[0].value];
  const question = createQuestion(questionType);

  questionContainer.className = "small-margin-top";
  questionContainer.append(question);

  question.firstChild.getElementsByClassName("input")[0].focus();
}

function addChoice(clickedElement) {
  const questionContainer = clickedElement.parentElement.parentElement;
  const choiceContainer = questionContainer.getElementsByClassName("choice-container")[0];
  const choiceField = createTextBox();

  choiceField.placeholder = "choice label"

  choiceContainer.append(choiceField);

  choiceField.focus();
}

function createQuestion(type) {
  const question = createQuestionContainer();

  switch (type) {
    case QuestionType.text: {
      const labelPrefix = "Text";

      question.append(createQuestionLabel(labelPrefix));

      break;
    }
    case QuestionType.choice: {
      const questionLabelPrefix = "Choice";

      question.append(createQuestionLabel(questionLabelPrefix));
      question.append(createChoiceContainer());
      question.append(createChoiceQuestionOption());

      break;
    }
    default:
      throw Error("QuestionTypeIsNotValid");
  }

  return question;
}

function createQuestionLabel(labelPrefix) {
  const container = createLabelContainer();

  container.append(createQuestionLabelText(labelPrefix));
  container.append(createTextBox());

  return container;
}

function createQuestionLabelText(labelPrefix) {
  const labelText = labelPrefix + " " + "Question Label";

  return createLabel(labelText);
}

function createChoiceQuestionOption() {
  const container = createChoiceOptionContainer();

  container.append(createAddChoiceButton());
  container.append(createMultipleSelectionOption());

  return container;
}

function createMultipleSelectionOption() {
  const container = createMultipleSelectionOptionContainer();

  container.append(createCheckbox());
  container.append(createLabel("Allow Multiple Selection"));

  return container;
}

function createQuestionContainer() {
  const container = document.createElement("div");
  
  container.className = "question input-container";
  
  return container;
}

function createLabelContainer() {
  const labelContainer = document.createElement("div");

  labelContainer.className = "label-container";

  return labelContainer;
}

function createChoiceContainer() {
  const container = document.createElement("div");
  
  container.className = "choice-container";
  
  return container;
}

function createChoiceOptionContainer() {
  const container = document.createElement("div");
  
  container.className = "option-container";
  
  return container;
}

function createMultipleSelectionOptionContainer() {
  const container = document.createElement("div");
  
  container.className = "multiple-selection-option-container";
  
  return container;
}

function createAddChoiceButton() {
  const addChoiceButton = document.createElement("button");

  addChoiceButton.className = "add-choice-button";
  addChoiceButton.textContent = "Add Choice";
  addChoiceButton.setAttribute("onclick", "addChoice(this)");

  return addChoiceButton;
}

function createLabel(text) {
  const label = document.createElement("label");

  label.textContent = text;

  return label;
}

function createTextBox() {
  const textBox = createInput();

  textBox.type = "text";
  textBox.className = "input";

  return textBox;
}

function createCheckbox() {
  const checkbox = createInput();

  checkbox.className = "checkbox";
  checkbox.type = "checkbox";

  return checkbox;
}

function createInput() {
  return document.createElement("input");
}

function setupView() {
  document.getElementById("poll-name-field").focus();
}

setupView();
