const user_id = JSON.parse(document.getElementById('user').textContent);
const otherUser = JSON.parse(document.getElementById('other_user').textContent);

function scrollDown(){
    chatThread = document.querySelector("#chat-thread");
    chatThread.scrollTop = chatThread.scrollHeight;
}

scrollDown();

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + otherUser
    + '/'
)

chatSocket.onmessage = function(e){
    const data = JSON.parse(e.data);
    console.log(data)
    sender_id = data.sender_id;
    
    if(user_id === sender_id){
        let msg_div = `<div class="my-text-div">
                        <div class="my-text-container">
                            <div class="my-text">${data.message}</div>
                        </div>
                    </div>`;
        const chatThread = document.querySelector("#chat-thread");
        chatThread.innerHTML += msg_div;
        scrollDown();
    } else {
        let msg_div = `<div class="friend-text-div">
                        <img
                            src='${data.sender_profile_pic}' />
                        <div class="friend-text-container">
                            <div class="friend-text">${data.message}</div>
                        </div>
                    </div>`;

        const chatThread = document.querySelector("#chat-thread");
        chatThread.innerHTML += msg_div;
        scrollDown();
    }

}

chatSocket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

chatSocket.onclose = function(e){
    console.log("CONNECTION LOST");
}

document.querySelector('#msg-txt').focus();
document.querySelector('#msg-txt').onkeyup = function(e) {
    if(e.keyCode === 13){
        sendMessage();
    }
}

const sendMessage = (e) => {
    const message = document.querySelector("#msg-txt").value;

    if (message === ''){
        return 
    }

    chatSocket.send(JSON.stringify({
        'message': message,
        'sender': user_id
    }));

    document.querySelector("#msg-txt").value = '';
    document.querySelector("#msg-txt").focus();
}

