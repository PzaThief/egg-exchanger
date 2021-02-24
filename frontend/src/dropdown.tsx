function Dropdown(units: Array<any>) {
  return (
    <div className="dropdown">
      <div className="control">
        <div className="selected-value">기준화폐를 입력해주세요</div>
        <div className="arrow" />
      </div>
      <div className="options">
        {units.map((unit: any) => (
          <div className="option">{unit.name}</div>
        ))}
      </div>
    </div>
  );
}

export default Dropdown;
