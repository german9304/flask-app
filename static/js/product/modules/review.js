import { createElement } from './helper/helper';

/**
 *
 * @param {array} reviews reviews from product api
 */
function createReviewElements(reviews) {
  const elReviews = reviews.map(({ comment, user_parent: userParent }) => {
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
  });
  return elReviews;
}
export default createReviewElements;
