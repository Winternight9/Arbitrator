function onVoteCheckboxClick(pollID) {
  const url = "/changeVoteAvailability/";
  const data = JSON.stringify({ pollID: pollID });

  $.ajax({
    url: url,
    method: "post",
    headers: { "X-CSRFToken": CSRF_TOKEN },
    data: data,
    success: response => {},
    error: error => {
      console.log(error);
    }
  });
}

function onResultCheckboxClick(pollID) {
  const url = "/changeResultAvailability/";
  const data = JSON.stringify({ pollID: pollID });

  $.ajax({
    url: url,
    method: "post",
    headers: { "X-CSRFToken": CSRF_TOKEN },
    data: data,
    success: response => {},
    error: error => {
      console.log(error);
    }
  });
}
