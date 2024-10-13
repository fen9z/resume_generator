document.getElementById("resume-form").addEventListener("input", function () {
  // 获取表单数据
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const education = document.getElementById("education").value;
  const experience = document.getElementById("experience").value;
  const skills = document.getElementById("skills").value;

  // 显示预览
  const previewDiv = document.getElementById("preview");
  previewDiv.innerHTML = `
      <h2>${name}</h2>
      <p>Email: ${email}</p>
      <p>Phone: ${phone}</p>
      <h3>Education</h3>
      <p>${education}</p>
      <h3>Experience</h3>
      <p>${experience}</p>
      <h3>Skills</h3>
      <p>${skills}</p>
  `;
  previewDiv.style.display = "block";
});
