document.getElementById("CommentBox").style.display = "none";
document.getElementById("CommentBox1").style.display = "none";
document.getElementById("CommentClick").addEventListener("click", () => {
  document.getElementById("CommentBox").style.display = "block";
});
document.getElementById("closeBTn").addEventListener("click", () => {
  document.getElementById("CommentBox").style.display = "none";
});
document.getElementById("CommentClick1").addEventListener("click", () => {
  document.getElementById("CommentBox1").style.display = "block";
});
document.getElementById("closeBTn1").addEventListener("click", () => {
  document.getElementById("CommentBox1").style.display = "none";
});
