var element = document.querySelector('.section-brackets'); 

/*
 * Call the polyfill
 *
 * patternID : the unique ID of the SVG pattern
 * patternURL : the URL to the background-image
 * class : the css-class applied to the SVG
 */
element.backgroundClipPolyfill({
  'patternID' : 'mypattern',
  'patternURL' : '../img/bg-title.jpg',
  'class' : 'section-brackets'
});
