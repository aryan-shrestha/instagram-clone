const like = (postId) => {
    const likeBtn = document.getElementById(`like-btn-${postId}`);
    const likeBtnPath = likeBtn.firstElementChild;
    const likedBtnPath = "M34.6 3.1c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5s1.1-.2 1.6-.5c1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z";
    const unlikedBtnPath = "M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z";
    const likesDiv = document.getElementById(`likes-div-${postId}`);
    const userProfilePic = likesDiv.dataset.userProfilePic;

    axios({
        method: 'get',
        url : `http://127.0.0.1:8000/like/${postId}/`,
        })
    .then((response)=>{
        if(response.data.liked){
            likeBtnPath.setAttribute("d", likedBtnPath);
            likeBtn.setAttribute("fill", "#ed4956");
            likesDiv.innerHTML = `
                                <img src="${userProfilePic}" alt="">
                                <p class="likes-cnt">
                                Liked by <span>You</span> and
                                <span>${response.data.total_likes-1}
                                    others
                                </span>
                                </p>
                                `;
        } else{
            likeBtnPath.setAttribute("d", unlikedBtnPath);
            likeBtn.setAttribute("fill", "#262626");
            likesDiv.innerHTML = `<p class="likes-cnt">
                                ${response.data.total_likes} Likes
                                </span>
                            </p>`
        }
    })
    .catch(err=>{
        console.log(err);
    }); 
}

const showPostCreateForm = () => {
    const createPostContainer = document.getElementById("create-post-container");
    createPostContainer.classList.remove("hidden");
}

const hidePostCreateForm = () => {
    const createPostContainer = document.getElementById("create-post-container");
    createPostContainer.classList.add("hidden");
}

const requestFollow = (userId) => {

    const followBtn = document.getElementById("follow-btn");

    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/followers/send_follow_request/${userId}/`,
    })
    .then((response)=>{
        if(response.data){
            followBtn.innerText = "Requested";
        }
    })
    .catch((err)=> {
        console.log(err);
    });
}

const unFollow = (userId) => {

    const unFollowBtn = document.getElementById("unfollow-btn");

    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/followers/unfollow_user/${userId}/`
    })
    .then((response)=>{
        if(response.data.unfollowed){
            unFollowBtn.innerText = "Follow";
            unFollowBtn.setAttribute("id", "follow-btn")
            unFollowBtn.setAttribute("onclick", `requestFollow(${userId})`);
        }
    })
    .catch((err)=>{
        console.log(err);
    });
}

const acceptFollowRequest = (request_id) => {
    
    const acceptBtn = document.getElementById("accept-btn");

    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/followers/accept_follow_request/${request_id}`,
    })
    .then((response)=>{
        if(response.data.follows_sender){
            acceptBtn.innerText = "Following";
            acceptBtn.disabled = true;
        }
        else{
            acceptBtn.innerText = "Follow Back";
            acceptBtn.setAttribute("id", "follow-btn");
            acceptBtn.setAttribute("onClick", `requestFollow(${response.data.sender_id})`);
        }       
    })
    .catch((err)=>{
        console.log(err);
    });
}