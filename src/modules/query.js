// SEARCH / AS @user answers ${questionNumber} /WHERE(num = ${optionNumber}) RETURN (@user->location AS result) FROM $0

function tokenize(query) {
  return query.match(/(\d+(?:\.\d+)?:\d+|[()&|!])/g);
}

function compile(query) {
  return tokenize(query).map(token => {
    switch(token) {
      case '!':
        return 'NOT';
      case '&':
        return 'AND';
      case '|':
        return 'OR';
      default:
        // gonna be a question-option thing
        const [question, option] = token.match(/(\d+(?:\.\d+)):(\d+)/).slice(1);
        return `(question = '${question}' AND option = ${option})`;
    }
  }).join(' ');
}
