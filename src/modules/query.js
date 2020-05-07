// SEARCH / AS @user answers ${questionNumber} /WHERE(num = ${optionNumber}) RETURN (@user->location AS result) FROM $0

function tokenize(query) {
  return query.match(/(\d+(?:\.\d+)?:\d+|[()&|!])/g);
}

function consumeOperation(ops, vals) {
  const op = ops.pop();
  vals.push({
    type: 'operation',
    value: op.value,
    children: Array.from({length: 2 - op.unary}, () => vals.pop())
  });
}


function parse(query) {
  const ops = [];
  const vals = [];
  let lastIsOperand = false;
  let allowUnary = true;

  for (const token of tokenize(query)) {
    switch (token) {
      case '&':
      case'|':
      case '!':
        const isUnary = !lastIsOperand;
        while (
          ops.length > 0
          && ops[ops.length - 1] !== '('
          && ops[ops.length - 1].unary > isUnary
        ) {
          consumeOperation(ops, vals);
        }
        if (isUnary && !allowUnary) {
          throw new Error('Invalid syntax (misplaced unary operator)');
        }
        ops.push({
          value: token,
          unary: isUnary
        });
        lastIsOperand = false;
        allowUnary = true;
        break;
      case '(':
        ops.push(token);
        lastIsOperand = false;
        allowUnary = true;
        break;
      case ')':
        while (ops[ops.length - 1] !== '(') {
          if (ops.length === 0) {
            throw new Error('Invalid syntax (too many right parentheses)');
          }
          consumeOperation(ops, vals);
        }
        ops.pop();
        lastIsOperand = null;
        allowUnary = false;
        break;
      default:
        const [question, option] = token.split(':');
        vals.push({type: 'operand', value: {question, option}});
        lastIsOperand = true;
        allowUnary = false;
    }
  }
  while (ops.length > 0) {
    if (ops[ops.length - 1] === '(') {
      throw new Error('Invalid syntax (too many left parentheses)');
    }
    consumeOperation(ops, vals);
  }
  return vals.pop();
}
