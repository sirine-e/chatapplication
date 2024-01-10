document.getElementById('EmojiButton').addEventListener('click', function (event) {
    event.preventDefault();//eviter que la page se recharge a chaque clic sur le bouton
    pickEmoji();
});

function pickEmoji(){
    var EmojiPicker = document.getElementById('EmojiPicker');
    EmojiPicker.style.display = (EmojiPicker.style.display === 'block') ? 'none' : 'block';
}

function addEmoji(emoji) {
    document.getElementById('chat-message-input').value += emoji;
}