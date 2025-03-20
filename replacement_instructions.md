# Placeholder Image Replacement Instructions

## Objective
Replace all placeholder images from via.placeholder.com with Fakeimg.pl generated images

## Replacement Rules
- Use grey background (#808080)
- Maintain original image dimensions
- Preserve original alt text
- Add descriptive text to images

## Replacement Template
```html
<!-- Original -->
<img src="https://via.placeholder.com/112x28" alt="MAD Communications Logo">

<!-- Replacement -->
<img src="http://fakeimg.pl/112x28/?bg=808080&text=MAD+Communications&font=arial" alt="MAD Communications Logo">
```

## Specific Image Replacements

### Logo Images (112x28)
- Text: "MAD Communications"
- URL: `http://fakeimg.pl/112x28/?bg=808080&text=MAD+Communications&font=arial`

### Partner Brand Images (120x80)
- Text: "Partner Brand"
- URL: `http://fakeimg.pl/120x80/?bg=808080&text=Partner+Brand&font=arial`

### Large Content Images (600x400)
1. Brand PR Service
   - URL: `http://fakeimg.pl/600x400/?bg=808080&text=Brand+PR+Service&font=arial`

2. Retail Market Entry
   - URL: `http://fakeimg.pl/600x400/?bg=808080&text=Retail+Market+Entry&font=arial`

### Team Images (150x150)
1. Britney Luo
   - URL: `http://fakeimg.pl/150x150/?bg=808080&text=Britney+Luo&font=arial`

2. Brad Phillips
   - URL: `http://fakeimg.pl/150x150/?bg=808080&text=Brad+Phillips&font=arial`

## Files to Update
1. index.html
2. service.html
3. about-us.html
4. contact.html

## Verification Checklist
- [ ] All placeholder images replaced
- [ ] Original alt text preserved
- [ ] Image dimensions maintained
- [ ] Grey background used consistently
- [ ] Descriptive text added to images
- [ ] Cross-browser compatibility checked

## Recommended Replacement Process
1. Open each HTML file
2. Use find-and-replace or manual editing
3. Replace `src` attributes with Fakeimg.pl URLs
4. Verify changes visually
5. Test website functionality