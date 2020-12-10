/*  The Counter    */

var countDownDate = new Date("March 26, 2020 08:00:00").getTime();
var interval = NaN

var x = setInterval(function () {
  var now = new Date().getTime();
  var distance = countDownDate - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  document.getElementById("timer").innerHTML = '<div><span class="day">' + days +
    " days </span><span class='hours'> " + hours + " hrs </span><span class='minutes'> " +
    minutes + " mins </span><span class='seconds'>" + seconds + "s </span>" + '</div>';
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "TODAY";
  }
}, 1000);


/*  The Payment Listener    */

function checkStatus() {
  fetch('https://eawaterspayments.herokuapp.com/ispaid')
    .then(response => {
      if (response.ok) {
        return response.json()
      } else {
        return
      }
    }).then(res => {
      if (res.status === 0) {
        var msg = res.body
        console.log(res)
        if (msg.BillRefNumber.toUpperCase() === ($('#first_name').val() + " " + $('#last_name')
            .val()).toUpperCase() ||
          msg.MSISDN === $('#phone').val()) {

          $('#is_paid').val('YES')
          $('#paymentstatus').html(
            "<div class='alert alert-success' role='alert'>Thank You. Payment Received for " +
            msg.BillRefNumber + "</div>")
          $('#mpesa_code').val(msg.TransID)
          $('#mpesa_name').val(msg.BillRefNumber)
          $('#mpesa_amount').val(msg.TransAmount)
          $("#finishBtn").prop('disabled', false)
          clearInterval(interval)
        }
      } else {
        console.log('.')
      }
    })
}


/*  The Step Navigation Listener    */


function goToNew(current, newstep,is_next) {
  var valid = true;
  var inputs = document.getElementById(current).getElementsByTagName("input")
  for (i = 0; i < inputs.length; i++) {
    if (inputs[i].value === "") {
      inputs[i].className += " invalid";
      valid = false;
    }
  }
  if (valid || !is_next) {
    $("#" + current).hide()
    $("#" + newstep).show()
  }
  if (newstep = "stepThree") {
    interval = setInterval(checkStatus, 100)
  }
}



function nameChanged() {
  $('#account_no').html(($('#first_name').val() + " " + $('#last_name').val()).toUpperCase())

}

$(function () {
  $('#country').change(function () {
    var selected = $(this).find('option:selected');
    var extra = selected.data('code');
    $('#country_code').html(extra)
  });

  $('#phone_no_part_two').change(function () {
    if ($('#phone_no_part_two').val().charAt(0) === '0') {
      $('#phone').val($('#country_code').html() + "" + $('#phone_no_part_two').val().substr(1))
    } else {
      $('#phone').val($('#country_code').html() + "" + $('#phone_no_part_two').val())
    }
  })
});

function limit(element) {
  var max_chars = 10;
  if (element.value.length > max_chars) {
    element.value = element.value.substr(0, max_chars);
  }
}