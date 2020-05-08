// SEARCH / AS @user answers ${questionNumber} /WHERE(num = ${optionNumber}) RETURN (@user->location AS result) FROM $0

function tokenize(query) {
  return query.match(/(\d+(?:\.\d+)?(?:\d+|\*)|[()&|!=])/g);
}

export function compile(query) {
  return tokenize(query).map(token => {
    switch(token) {
      case '!':
        return 'NOT';
      case '&':
        return 'AND';
      case '|':
        return 'OR';
      case '(':
      case ')':
      case '=':
        return token;
      default:
        // hacc
        if (token.includes('*')) {
          const question = token.match(/(\d+(?:\.\d+)?):\*/)[1];
          return `-1 IN ${question}`;
        }
        const [question, option] = token.match(/(\d+(?:\.\d+)?):(\d+)/).slice(1);
        return `[${question}]->${option}`;
    }
  }).join(' ');
}
