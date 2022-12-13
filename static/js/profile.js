const popOut = (postId)=>{
    const post = document.getElementById(postId);
    document.getElementById("pop-out-card-username").innerText = post.dataset.username;
    document.getElementById("likes-cnt").innerText = `${post.dataset.totalLikes} likes `;
    document.getElementById("post-time").innerText = `${post.dataset.dateCreated}`;
    document.getElementById("pop-out-card-user-profile-pic").setAttribute("src", post.dataset.userProfilePic)
    document.getElementById("pop-out-card-post-image").setAttribute("src", post.children[0].children[0].getAttribute("src"))
    document.getElementById("pop-out-wrapper").classList.remove('hidden');

    console.log(post.children[0].children[0].getAttribute("src"));
}

const closeBtn = () => {
    const popOutDiv = document.getElementById("pop-out-wrapper");
    popOutDiv.classList.add("hidden");
}