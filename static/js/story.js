const popOutWrapper = document.getElementById("pop-out-wrapper");

const closePopOut = () => {
    popOutWrapper.classList.add("hidden");
}

const previewStory = (storyId) => {
    popOutWrapper.classList.remove("hidden");
    const mainContainer = document.getElementById("main-container");
    const storyCard = document.getElementById(`story-${storyId}`);
    const storyUsername = document.getElementById("story-preview-user-username");
    const storyProfilePic = document.getElementById("story-preview-user-profile-pic");
    const storyPic = document.getElementById("story-preview-story-pic");

    storyUsername.innerText = storyCard.dataset.storyUserUsername;
    storyProfilePic.setAttribute('src', storyCard.dataset.storyUserProfilePic);
    storyPic.setAttribute('src', storyCard.dataset.storyPic);
    storyCard.children[0].classList.replace("unseen", "seen");
    mainContainer.style.overflow = "hidden"
    
}

const nextStory = () => {
    const stories = Array.from(document.querySelectorAll(".story-card"));
    stories.shift();
    const storyCnt = stories.length;
    let currentIndex = 0;
    stories.forEach(element => {
        if(document.getElementById("story-preview-story-pic").getAttribute('src') === element.dataset.storyPic){
            currentIndex = stories.indexOf(element);
        }
    });
    console.log("currentIndex: ", currentIndex);
    console.log("storyCnt: ", storyCnt);
    if((currentIndex + 1) == storyCnt){
        stories[currentIndex].children[0].classList.replace("unseen", "seen");
        closePopOut();
        return;
    } else{
        document.getElementById("story-preview-user-profile-pic").setAttribute('src', stories[currentIndex + 1].dataset.storyUserProfilePic);
        document.getElementById("story-preview-user-username").innerText = stories[currentIndex + 1].dataset.storyUserUsername;
        document.getElementById("story-preview-story-pic").setAttribute('src', stories[currentIndex + 1].dataset.storyPic);
        stories[currentIndex].children[0].classList.replace("unseen", "seen");
    }
}
