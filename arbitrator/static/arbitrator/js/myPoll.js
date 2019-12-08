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

function onRemovePollClick(pollID) {
  const userConfirm = confirm("Remove?");

  if (userConfirm) {
    const url = "/removePoll/";
    const data = JSON.stringify({ pollID: pollID });

    $.ajax({
      url: url,
      method: "post",
      headers: { "X-CSRFToken": CSRF_TOKEN },
      data: data,
      success: response => {
        location.reload();
      },
      error: error => {
        console.log(error);
      }
    });
  }
}
