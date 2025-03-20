# Placeholder Image Replacement Plan with Fakeimg.pl

## Detailed Replacement Strategy

### Manual Replacement Process
For each HTML file, follow these steps:
1. Find all `<img>` tags with `src` containing "via.placeholder.com"
2. Replace the `src` attribute with corresponding Fakeimg.pl URL
3. Preserve the original `alt` text
4. Maintain the original image dimensions

### Replacement Template
```html
<!-- Original -->
<img src="https://via.placeholder.com/112x28" alt="MAD Communications Logo">

<!-- Replaced -->
<img src="http://fakeimg.pl/112x28/?bg=808080&text=MAD+Communications&font=arial" alt="MAD Communications Logo">
```

### Files to Update
1. index.html
2. service.html
3. about-us.html
4. contact.html

### Specific Replacement Rules
- Logo images (112x28): Add "MAD Communications" text
- Partner Brand images (120x80): Add "Partner Brand" text
- Large content images (600x400): Add descriptive text
- Team/Personal images (150x150): Add name text

### Verification Checklist
- [ ] All placeholder images replaced
- [ ] Original alt text preserved
- [ ] Image dimensions maintained
- [ ] Grey background (#808080) used consistently
- [ ] Text added to each image
- [ ] Cross-browser compatibility checked

## Implementation Notes
- Use a text editor or find-and-replace functionality
- Manually edit each HTML file
- Double-check replacements after editing

## Potential Challenges
- Ensuring consistent text sizing
- Maintaining design integrity
- Verifying responsive design

## Next Steps
1. Manually replace images in each HTML file
2. Test website functionality
3. Verify visual consistency
