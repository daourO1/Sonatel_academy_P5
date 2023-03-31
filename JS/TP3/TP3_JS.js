const button = document.getElementsByClassName("notification")
button.addEventListener("click",()=>{
    const color = button.style.backgroundColor;
    let notificationType = "";
    switch (color) {
        case "rgb(55, 140, 55)":
            notificationType = "Notification Success";
            break;
       // case "red":
         //   notificationType = "Notification Danger";
           // break;
        //case "yellow":
          //  notificationType = "Notification Waming";
            //break;
        //case "rgb(4, 129, 218)":

    }
    showNotification(notificationType);
})
const notificationContainer = document.createElement('div');
notificationContainer.classList.add('notification-container');
document.body.appendChild(notificationContainer);

function showNotification(type) {
  const notification = document.createElement('div');
  notification.classList.add('notification', type);
  notification.textContent = type.toUpperCase();
  notificationContainer.appendChild(notification);
  setTimeout(() => {
    notification.remove();
  }, 1000);
}