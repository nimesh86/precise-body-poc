const API_URL = "http://127.0.0.1:8000/api/v1/generate";

function bindSlider(sliderId, valueId) {
  const slider = document.getElementById(sliderId);
  const value = document.getElementById(valueId);

  value.textContent = Number(slider.value).toFixed(2);

  slider.addEventListener("input", () => {
    value.textContent = Number(slider.value).toFixed(2);
  });
}
bindSlider("height", "heightValue");
bindSlider("chest", "chestValue");
bindSlider("waist", "waistValue");
bindSlider("hips", "hipsValue");
bindSlider("body_fat", "bodyFatValue");



document.getElementById("generate").addEventListener("click", async () => {
  const payload = {
    meta: { schema_version: "1.0" },
    body: {
      gender: document.getElementById("gender").value,
      age: Number(document.getElementById("age").value),
      height: Number(document.getElementById("height").value),
      chest: Number(document.getElementById("chest").value),
      waist: Number(document.getElementById("waist").value),
      hips: Number(document.getElementById("hips").value),
      body_fat: Number(document.getElementById("body_fat").value),
    },
  };

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const result = await response.json();

  console.log(result);
  if (result.preview_image) {
    
    // backend returns relative path, so prepend server URL
    document.getElementById("previewImage").src =
      "http://127.0.0.1:8000/" + result.preview_image;
  }
});
