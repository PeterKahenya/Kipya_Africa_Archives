var interval=NaN;
function nextOne() {
    $("#about-you").hide()
    $("#your-contacts").show()
}

function nextTwo() {
    $("#your-contacts").hide()
    $("#finish").show()
    checkRole()
}

function prevOne() {
    $("#about-you").show()
    $("#your-contacts").hide()
}

function prevTwo() {
    $("#finish").hide()
    $("#your-contacts").show()
}

function sendpfi() {
    console.log({
        first_name: $('#first_name').val(),
        last_name: $('#last_name').val(),
        phone: $('#phone_no_val').val(),
        email: $('#email_addr').val(),
        assoc: "GAK",
        role: $('#role').val(),

    })
    fetch('https://eawaterspayments.herokuapp.com/sendpfi', {
        
        method: 'POST',
        body: JSON.stringify({
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            phone: $('#phone_no_val').val(),
            email: $('#email_addr').val(),
            assoc: "GAK",
            role: $('#role').val(),

        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(response => response.json()).then(response => {
        console.log(response)
    })
}

function registrationDone() {
    $("#reg_form").hide();
    $("#success_message").show();
    sendpfi()
}

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
                    msg.MSISDN === $('#phone_no_val').val()) {

                    $('#ispaid').val('YES')

                    $('#paymentstatus').html(
                        "<div class='alert alert-success' role='alert'>Thank You Payment Received for " +
                        msg.BillRefNumber + "</div>")
                    $('#mpesa_code').val(msg.TransID)
                    $('#mpesa_name').val(msg.BillRefNumber)
                    $('#mpesa_amount').val(msg.TransAmount)
                    enableFinishPayment()
                    clearInterval(interval)
                }
            } else {
                console.log('waiting for payment')
            }
        })
}

function checkRole() {
    if ($('#role').val() === "Kenyan Delegate"||$('#country').val() === "Kenya") {
        document.getElementById('mpesa_step').style.display = 'block'
        interval = setInterval(checkStatus, 100)
    } 
}

function limit(element) {
    var max_chars = 10;

    if (element.value.length > max_chars) {
      element.value = element.value.substr(0, max_chars);
    }
}

$(function () {

    $('#country').change(function () {
      var selected = $(this).find('option:selected');
      var extra = selected.data('code');
      $('#code').html(extra)
    });

    $('#phone_no').change(function () {
      if ($('#phone_no').val().charAt(0) === '0') {
        $('#phone_no_val').val($('#code').html() + "" + $('#phone_no').val().substr(1))
      } else {
        $('#phone_no_val').val($('#code').html() + "" + $('#phone_no').val())
      }
    })
  });
