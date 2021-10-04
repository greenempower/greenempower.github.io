background_color_base_rgb = [174, 185, 153];

background_color_scalar = 0.5;

background_color_rgb = [
	background_color_base_rgb[0] * background_color_scalar,
	background_color_base_rgb[1] * background_color_scalar,
	background_color_base_rgb[2] * background_color_scalar
];

r = background_color_rgb[0];
g = background_color_rgb[1];
b = background_color_rgb[2];

fmt = `rgb(${r}, ${g}, ${b})`;
//document.body.style.backgroundColor = fmt;

