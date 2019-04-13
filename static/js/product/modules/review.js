import { createElement } from './helper/helper';
import { post } from '../api/api';


/**
 *
 * @param {object} data comment to post
 */
async function createReviewAPI(data) {
  const options = {
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify(data),
  };
  return post('/api/review/', options);
}

/**
 *
 * @param {string} comment comment to be created
 * @param {number} id id from product
 */
function createReview(comment, id) {
  return {
    product: id,
    comment,
  };
}

function createReviewElement({ comment, user_parent: userParent }) {
  const section = createElement('section', { className: 'review-content' });
  const sectionUserReview = createElement('section', { className: 'user-review' });
  const { username } = userParent;
  sectionUserReview.innerHTML = `
      <p> ${username}</p>
    `;
  const sectionReview = createElement('section', { className: 'review' });
  sectionReview.innerHTML = `
      <p> ${comment}</p>
    `;
  section.appendChild(sectionUserReview);
  section.appendChild(sectionReview);
  return section;
}

/**
 *
 * @param {array} reviews reviews from product api
 */
function createReviewElements(reviews) {
  return reviews.map(review => createReviewElement(review));
}


export {
  createReviewElements,
  createReviewAPI,
  createReview,
  createReviewElement,
};
