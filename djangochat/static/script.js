document.getElementById('EmojiButton').addEventListener('click', function (event) {
    event.preventDefault();//Avoid the page reloading on click
    pickEmoji();
});

function pickEmoji(){
    var EmojiPicker = document.getElementById('EmojiPicker');
    //If display is 'block' change it to 'none', else change to 'block'
    EmojiPicker.style.display = (EmojiPicker.style.display === 'block') ? 'none' : 'block';
}

function addEmoji(emoji) {
    document.getElementById('chat-message-input').value += emoji;
}