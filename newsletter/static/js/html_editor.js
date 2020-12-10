const editor = document.getElementsByClassName('editor')[0];
const toolbar = editor.getElementsByClassName('toolbar')[0];
const buttons = toolbar.querySelectorAll('.editor_btn:not(.has-submenu)');


for(let i = 0; i < buttons.length; i++) {
  let button = buttons[i];

  button.addEventListener('click', function(e) {
    let action = this.dataset.action;

    if(action === 'code') {
      const contentArea = editor.getElementsByClassName('content-area')[0];
      const visuellView = contentArea.getElementsByClassName('visuell-view')[0];
      const htmlView = contentArea.getElementsByClassName('html-view')[0];

      if(this.classList.contains('active')) { // show visuell view
        visuellView.innerHTML = htmlView.value;
        htmlView.style.display = 'none';
        visuellView.style.display = 'block';
        this.classList.remove('active');
      } else {  // show html view
        htmlView.innerText = visuellView.innerHTML;
        visuellView.style.display = 'none';
        htmlView.style.display = 'block';
        this.classList.add('active');
      }

      return false;
    }

    document.execCommand(action, false);
  });
}

