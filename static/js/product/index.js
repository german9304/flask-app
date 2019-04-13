// import Review from './modules/review';
import { fetchProducts, fetchProduct } from './modules/products';
import createReviewElements from './modules/review';
import spinner from './modules/spinner';


const state = {
  product: {},
  user: {},
};

const url = new URL(document.location); // url
const productReviews = document.getElementById('product-reviews');
const formReviewComments = document.getElementById('form-review__comments');

productReviews.appendChild(spinner);

// console.log(url.searchParams.get('id'));

fetchProducts('/api/products')
  .then(data => console.log(data));

const productId = url.searchParams.get('id');


fetchProduct(`/api/product/${productId}`)
  .then(({ data }) => {
    const fragment = document.createDocumentFragment();
    const reviews = createReviewElements(data.reviews_assoc);
    reviews.forEach(review => fragment.appendChild(review));
    // console.log(reviews);
    spinner.remove();
    productReviews.appendChild(fragment);
  });


function handleAddReview(e) {
  e.preventDefault();
  console.log('submited');
}

formReviewComments.addEventListener('submit', handleAddReview);
